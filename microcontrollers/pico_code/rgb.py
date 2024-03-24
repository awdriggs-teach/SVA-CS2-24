import board
import adafruit_rgbled

# Pin the Red LED is connected to
RED_LED = board.GP5

# Pin the Green LED is connected to
GREEN_LED = board.GP6

# Pin the Blue LED is connected to
BLUE_LED = board.GP7

# Create a RGB LED object
led = adafruit_rgbled.RGBLED(RED_LED, BLUE_LED, GREEN_LED)

while True:
    led.color = (107, 235, 52) #greenish blue



