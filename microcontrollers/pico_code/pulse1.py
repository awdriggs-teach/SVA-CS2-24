# Example of using PWM to fade a led light in and out
import board
import analogio #module for analog i/o
import pwmio #module for pulse widht modulation

pot = analogio.AnalogIn(board.GP26) #sets p
led = pwmio.PWMOut(board.GP14, frequency=1000)
direction = 1
freq = 8
count = 1

while True:
    # check edges
    if(freq >= 15 or freq < 1):
        direction = direction * -1 #change directions
        print("change dir")
    
    freq = freq + (1 * direction)
    #freq *= direction
    print(freq)
    led.duty_cycle = int(2 ** freq)
    #led.duty_cycle = pot.value
    
    time.sleep(0.1)
