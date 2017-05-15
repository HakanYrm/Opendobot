from dobot import Dobot

def TouchTest(x1, x2, y1, y2, xRange, yRange, xBuffer, yBuffer, up, down ,speed, acceleration):
    for x in my_range(x1 + xBuffer, x2 - xBuffer, xRange):
        for y in my_range(y1 + yBuffer, y2 - yBuffer, yRange):
            dobot.MoveWithSpeed(x, y, up, speed, acceleration)
            #raw_input("Press Enter to continue...")
            dobot.MoveWithSpeed(x, y, down, speed, acceleration)
            dobot.MoveWithSpeed(x, y, up, speed, acceleration)


def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
