"""Example for Pico. Morse Code, smart version""" 
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

long = 1
short = 0.25

msg = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.." #hello world

for l in msg:
    if l == " ": # space between letters
        time.sleep(long*2)
    else: 
        led.value = True
        
        if l == "-": 
            time.sleep(long)
        elif l == ".":
            time.sleep(short)
        
        led.value = False 
        time.sleep(short)  #pause between dots or dashes

print(msg)

