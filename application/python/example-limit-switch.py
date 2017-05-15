#! /usr/bin/env python
'''
An example running a calibration procedure using a limit switch/photointerrupter connected to a any
of the unused pins on Arduino, enabling/disabling pullup, specifying the switch type (normal LOW or
normal HIGH), forward joint rotation direction (towards the switch), forward and backward speeds.

Refer to DobotDriver.CalibrateJoint() for details.

This example works well with a photointerrupter shown on open-dobot/docs/images/interrupter*.jpg
It is cheap and easily mounted and yet sturdy and reliably. Requires minimum effort to get accurate
calibration for Joint1 (base), which originally has no sensors.
You can get an interrupter here:
https://www.sparkfun.com/products/9299
https://www.sparkfun.com/products/9322
		Initiates joint calibration procedure using a limit switch/photointerrupter. Effective immediately.
		Current command buffer is cleared.
		Cancel the procedure by issuing EmergencyStop() is necessary.
		
		@param joint - which joint to calibrate: 1-3
		@param forwardCommand - command to send to the joint when moving forward (towards limit switch);
				use freqToCmdVal()
		@param backwardCommand - command to send to the joint after hitting  (towards limit switch);
				use freqToCmdVal()
		@param direction - direction to move joint towards limit switch/photointerrupter: 0-1
		@param pin - firmware internal pin reference number that limit switch is connected to;
					refer to dobot.h -> calibrationPins
		@param pinMode - limit switch/photointerrupter normal LOW = 0, normal HIGH = 1
		@param pullup - enable pullup on the pin = 1, disable = 0
		@return True if command succesfully received, False otherwise.
'''

from dobot import DobotDriver
driver = DobotDriver('COM5')
#driver = DobotDriver('/dev/tty0')
driver.Open()

# Rotate base CW at 400 steps/s until limit switch is hit. Then retract CCW at 50 steps/s
# until switch is released and stop.
# Switch is expected to be connected (soldered) to pin D8 and pulled up (HIGH) externally (with a
# resistor, e.g. 4.7k, to 5V supply) or be an active device (like a photointerrupter). Pullup is not enabled on that pin.

# CalibrateJoint(self, joint, forwardCommand, backwardCommand, direction, pin, pinMode, pullup)
# driver.CalibrateJoint(1, driver.freqToCmdVal(1000), driver.freqToCmdVal(50),1,5, 0, 0) Manuel switch ile calisan kod
driver.CalibrateJoint(1, driver.freqToCmdVal(1000), driver.freqToCmdVal(50),1 , 5, 1, 0)




