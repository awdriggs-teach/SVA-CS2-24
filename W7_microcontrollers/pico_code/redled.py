"""
LED example for Pico. Blinks external LED on and off.

REQUIRED HARDWARE:
* LED on pin GP14.
"""
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP14)  # sets led to be line 14
led.direction = digitalio.Direction.OUTPUT  #

while True:  # infinite loop here
    led.value = True  # on
    time.sleep(0.25)
    led.value = False  # off
    time.sleep(0.25)

