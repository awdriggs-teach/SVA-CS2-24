import board
import analogio
import pwmio

pot = analogio.AnalogIn(board.GP26)
led = pwmio.PWMOut(board.GP14, frequency=1000)

while True:
    led.duty_cycle = pot.value
    

