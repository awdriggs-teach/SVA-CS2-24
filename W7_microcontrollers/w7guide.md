# Week 7 - Soldering and Microcontrollers

## Soldering
Soldering is an essential skill for making electronic experiments permanent! 
 
### Soldering Resources
- [Sparkfun Guide](https://learn.sparkfun.com/tutorials/how-to-solder-through-hole-soldering/all#soldering-your-first-component)
- [Contact Mic Instructables](https://www.instructables.com/How-to-Make-a-Contact-Microphone/)

## Microcontrollers  
A microcontroller is a simple, and cheap, computing device. They perform all sorts of functions but are generally used in embedded systems and offer input and output.
Meaning you can connect sensors, buttons, light, and motors! A microcontroller is program using another computer, and the code is loaded on the controller and then immediately begins to run.

We will be using a Raspberry Pi Pico. This microcontroller uses the increasingly popular RP2040 Chip. You can program it using C, micropython or CircuitPython, which I will use for examples.

### Getting Started
Follow [this guide](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython) to load CircuitPython onto your pico board.

Download the [Mu Editor](https://codewith.mu/) to begin coding your pico. 

### 'Hello World' Program
Here is a simple program. It will flash the onboard light forever. 

```python
"""Example for Pico. Turns the built-in LED on and off with no delay."""
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
```

### Python Crash Course
Check out [my python crash course](python.md) for getting started with CircuitPython.
 
## Microcontroller Resources
- [Full Adafruit Guide](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython?view=all)
- [Pico Projects](https://hackaday.com/tag/raspberry-pi-pico/)

