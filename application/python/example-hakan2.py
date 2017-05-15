#! /usr/bin/env python
import time
from dobot import Dobot
dobot = Dobot('COM5', debug=True)

down=50.3
up=53
acceleration = 150 # Acceleration in mm/s^2
speed = 150
dobot.CalibrateJoint(1, dobot.freqToCmdVal(50), dobot.freqToCmdVal(50), 1, 5, 1, 0)
dobot.InitializeAccelerometers()

testCycleNumber = 1

ph4x1 = 108  # phone 4 x1 position
ph4x2 = ph4x1 + 123.7  # phone 4 x2 position #real length = 12.1cm
ph4x3 = ph4x2 + 2.2
ph4x4 = ph4x1 + 2.2

ph4y1 = 133.4  # phone 4 y1 position
ph4y2 = ph4y1 - 4.2  # ph4y2 = ph4y1 + 68.1  # phone 4 y2 position #real length = 6.8cm
ph4y3 = ph4y2 + 68.4
ph4y4 = ph4y3 + 3.8

numberOfSquareX = 16.0
numberOfSquareY = 9.0

xRange = (ph4x2-ph4x1)/numberOfSquareX
yRange = (ph4y3-ph4y1)/numberOfSquareY

xBuffer = (xRange/2.0)
yBuffer = (yRange/2.0)

def pushTouchTestStartButton():
    dobot.MoveWithSpeed(ph4x1 + 105, ph4y1 + 34, up, speed, acceleration)
    dobot.MoveWithSpeed(ph4x1 + 105, ph4y1 + 34, down, speed, acceleration)
    dobot.MoveWithSpeed(ph4x1 + 105, ph4y1 + 34, up, speed, acceleration)
def TouchTest(x1, x2, y1, y2, xxRange, yyRange, xxBuffer, yyBuffer, upp, downn ,speedd, accelerationn):
    for x in my_range(x1 + xxBuffer, x2 - xxBuffer + 1.0, xxRange):
        for y in my_range(y1 + yyBuffer, y2 - yyBuffer + 1.0, yyRange):
            dobot.MoveWithSpeed(x, y, upp, speedd, accelerationn)
            dobot.MoveWithSpeed(x, y, downn, speed, accelerationn)
            dobot.MoveWithSpeed(x, y, upp, speed, accelerationn)
def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

for cycle in range(0, testCycleNumber):
    print testCycleNumber
    pushTouchTestStartButton()
    #  TouchTest(x1, x2, y1, y2, xRange, yRange, xBuffer, yBuffer, up, down, speed, acceleration)
    TouchTest(ph4x1,ph4x2,ph4y1,ph4y3,xRange,yRange,xBuffer,yBuffer, up, down, speed, acceleration)
    dobot.Wait(10)

# dobot.MoveWithSpeed(ph4x1, ph4y1, up, speed, acceleration)#x1,y1
# raw_input("Press Enter to continue...")

# dobot.MoveWithSpeed(ph4x2, ph4y2, up, speed, acceleration)#x2,y2
# raw_input("Press Enter to continue...")
#
# dobot.MoveWithSpeed(ph4x3, ph4y3, up, speed, acceleration)#x3,y3
# raw_input("Press Enter to continue...")

# dobot.MoveWithSpeed(ph4x4, ph4y4, up, speed, acceleration)#x4,y4
# raw_input("Press Enter to continue...")



# dobot.MoveWithSpeed(ph4x1, ph4y1-2.0+(68.1+1.5), up, speed, acceleration)#x2,y1
# raw_input("Press Enter to continue...")

#go to home
#raw_input("Press Enter to go home...")
dobot.MoveWithSpeed(260, -20, 80, speed, acceleration)

