import board
import digitalio
import time

dc = digitalio.DigitalInOut(board.GP10)
dc.direction = digitalio.Direction.OUTPUT

while True:
    dc.value = True
