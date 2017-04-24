#! /usr/bin/env python

import time
from dobot import Dobot
dobot = Dobot('COM3', debug=True)

# The top Z to go to.
up = 50
# The bottom Z to go to.
down = 50
# Maximum speed in mm/s
speed = 400
# Acceleration in mm/s^2
acceleration = 300

# Enable calibration routine if you have a limit switch/photointerrupter installed on the arm.
# See example-switch.py for details.
# Move both arms to approximately 45 degrees.
# Re-initialize accelerometers at approx. 45 degrees for the best result. Available on RAMPS only.

#dobot.MoveWithSpeed(260.0, 0.0, 85, 700, acceleration)
#time.sleep(2)
#dobot.InitializeAccelerometers()
#dobot.CalibrateJoint(1, dobot.freqToCmdVal(2000), dobot.freqToCmdVal(50), 1, 5, 1, 0)
dobot.CalibrateJoint(1, dobot.freqToCmdVal(1000), dobot.freqToCmdVal(50),1 , 5, 1, 0)


#Line
dobot.MoveWithSpeed(200.0, 80.0, up, speed, acceleration)
#dobot.MoveWithSpeed(200.0, 80.0, down, speed, acceleration)
#dobot.MoveWithSpeed(200.0, -90.0, down, speed, acceleration)
#dobot.MoveWithSpeed(200.0, -90.0, up, speed, acceleration)

# dobot.MoveWithSpeed(200.0, -90.0, down, speed, acceleration)
# dobot.MoveWithSpeed(200.0, 80.0, down, speed, acceleration)
# dobot.MoveWithSpeed(200.0, 80.0, up, speed, acceleration)
# dobot.MoveWithSpeed(200.0, -90.0, up, speed, acceleration)

# Rectangle with zig-zag inside
# dobot.MoveWithSpeed(170.0, -90.0, up, speed, acceleration)
# dobot.MoveWithSpeed(170.0, -90.0, down, speed, acceleration)
#dobot.MoveWithSpeed(170.0, 80.0, down, speed, acceleration)
#dobot.MoveWithSpeed(230.0, 80.0, down, speed, acceleration)
#dobot.MoveWithSpeed(230.0, -90.0, down, speed, acceleration)
#dobot.MoveWithSpeed(170.0, -90.0, down, speed, acceleration)
# x = 230
#y = 0
#for y in range(-90, 81, 5):
#	if x == 170:
#		x = 230
#	else:
#		x = 170
#	dobot.MoveWithSpeed(x, y, down, speed, acceleration)
#
#dobot.MoveWithSpeed(x, y, up, speed, acceleration)
#dobot.MoveWithSpeed(200.0, -90.0, up, speed, acceleration)
# Jog
#while True:
# 	dobot.MoveWithSpeed(200.0, 80.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, 80.0, down, speed, acceleration)
 #	dobot.MoveWithSpeed(200.0, 80.0, up, speed, acceleration)
 #	dobot.MoveWithSpeed(200.0, 80.0, 200, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -80.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -80.0, down, speed, acceleration)
#	dobot.MoveWithSpeed(200.0, -80.0, up, speed, acceleration)

# Dashed line
# while True:
# 	dobot.MoveWithSpeed(200.0, 80.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, 80.0, down, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, 70.0, down, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, 70.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, 40.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, 40.0, down, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, 30.0, down, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, 30.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, 0.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, 0.0, down, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -10.0, down, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -10.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -40.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -40.0, down, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -50.0, down, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -50.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -80.0, up, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -80.0, down, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -90.0, down, speed, acceleration)
# 	dobot.MoveWithSpeed(200.0, -90.0, up, speed, acceleration)
