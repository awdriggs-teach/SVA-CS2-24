import board
import analogio
import pwmio

pot = analogio.AnalogIn(board.GP26) #setup a ADC pin
led = pwmio.PWMOut(board.GP14, frequency=1000)

while True:
    led.duty_cycle = pot.value #set to poteniometer input, between 0 and 65534
    

