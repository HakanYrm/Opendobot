#! /usr/bin/env python

import time
from dobot import Dobot
dobot = Dobot('COM5', debug=True)



# Acceleration in mm/s^2
acceleration = 50
speed = 50

#go home
#raw_input("Press Enter to go home...")
#dobot.MoveWithSpeed(140, -200, 80, speed, acceleration)
dobot.MoveWithSpeed(140, -210, 80, speed, acceleration)
