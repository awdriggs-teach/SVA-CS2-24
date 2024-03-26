# Example of using PWM to fade a led light in and out
import board
import analogio #module for analog i/o
import pwmio #module for pulse widht modulation

pot = analogio.AnalogIn(board.GP26) #sets p
led = pwmio.PWMOut(board.GP14, frequency=1000)

direction = 1
value = 2**15 #used duty cycle, a 16bit positive integer. so this is 50%
step = 10 #changing the step will make the values changes faster or slower

while True:
    # check edges
    if(value > 65534):
        value = 65534
        direction *= -1
    elif (value < 0):
        value = 0
        direction *= -1
    
    #led.duty_cycle = pot.value
    led.duty_cycle = value
    
    print(value)
    value += step * direction #update value for next cycle
    


