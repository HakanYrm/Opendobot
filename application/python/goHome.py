#! /usr/bin/env python

import time
from dobot import Dobot
dobot = Dobot('COM5', debug=True)


# Acceleration in mm/s^2
acceleration = 20
speed = 20


dobot.InitializeAccelerometers()
dobot.CalibrateJoint(1, dobot.freqToCmdVal(500), dobot.freqToCmdVal(50),1 , 5, 1, 0)
dobot.MoveWithSpeed(260, -10, 80, speed, acceleration)

#go home
#raw_input("Press Enter to go home...")
# dobot.MoveWithSpeed(240, -100, 45, speed, acceleration)
# dobot.MoveWithSpeed(240, 100, 45, speed, acceleration)
