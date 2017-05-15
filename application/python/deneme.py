down=50.3
up=53
acceleration = 150 # Acceleration in mm/s^2
speed = 150

testCycleNumber = 1

ph4x1 = 108  # phone 4 x1 position
ph4x2 = ph4x1 + 123.7  # phone 4 x2 position #real length = 12.1cm
ph4x3 = ph4x2 + 2.2
ph4x4 = ph4x1 + 2.2

ph4y1 = 133.4  # phone 4 y1 position
ph4y2 = ph4y1 - 4.2  # ph4y2 = ph4y1 + 68.1  # phone 4 y2 position #real length = 6.8cm
ph4y3 = ph4y2 + 68.4
ph4y4 = ph4y3 + 3.8

shiftY = ph4y2 - ph4y1  # -4.2
shiftX = ph4x3 - ph4x2  # 2.2

numberOfSquareX = 16
numberOfSquareY = 9

xRange = (ph4x2-ph4x1)/numberOfSquareX
yRange = (ph4y4-ph4y1)/numberOfSquareY

xBuffer = (xRange/2.0)
yBuffer = (yRange/2.0)


def TouchTest(x1,y1,xxRange,yyRange,xxBuffer,yyBuffer,upp,downn,speedd,accelerationn,numberOfSquareXX,numberOfSquareYY,
              shiftXX,shiftYY):
    for stepX in range(0,numberOfSquareXX):
        x = x1 + xxRange * stepX + xxBuffer
        for stepY in range(0, numberOfSquareYY):
            y = y1 + yyRange * stepY + yyBuffer + stepX * (shiftYY/numberOfSquareXX)
            x = x + shiftXX/numberOfSquareYY
            print stepY *(shiftXX/numberOfSquareYY)

TouchTest(ph4x1, ph4y1, xRange, yRange, xBuffer, yBuffer, up, down, speed, acceleration, numberOfSquareX,
                      numberOfSquareY,
                      shiftX, shiftY)
