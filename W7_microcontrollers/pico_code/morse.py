
"""Example for Pico. morse code, hello, long way."""
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

long = 0.5
short = 0.25

# .... . .-.. .-.. ---

# h
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

time.sleep(short)

led.value = True
time.sleep(short)
led.value = False

time.sleep(long * 2)

# e
led.value = True
time.sleep(short)
led.value = False

time.sleep(long * 2)

# l
led.value = True
time.sleep(short)
led.value = False

time.sleep(short)

led.value = True
time.sleep(long)
led.value = False

time.sleep(short)

led.value = True
time.sleep(short)
led.value = False

time.sleep(short)

led.value = True
time.sleep(short)
led.value = False

time.sleep(long * 2)

# l
led.value = True
time.sleep(short)
led.value = False

time.sleep(short)

led.value = True
time.sleep(long)
led.value = False

time.sleep(short)

led.value = True
time.sleep(short)
led.value = False

time.sleep(short)

led.value = True
time.sleep(short)
led.value = False

time.sleep(long * 2)

# o
led.value = True
time.sleep(long)
led.value = False

time.sleep(short)

led.value = True
time.sleep(long)
led.value = False

time.sleep(short)

led.value = True
time.sleep(long)
led.value = False

print("done")

