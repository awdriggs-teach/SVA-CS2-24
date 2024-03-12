
"""Example for Pico. Flashes on board light three times."""
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

long = 0.5
short = 0.25

# flash light 3 times
led.value = True

time.sleep(short)

led.value = False

time.sleep(short)

led.value = True

time.sleep(short)

led.value = False

time.sleep(short)

led.value = True

time.sleep(short)

led.value = False

