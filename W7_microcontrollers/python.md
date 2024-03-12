# Python Crash Course
CircuitPython is based on MicroPython which is a slimmed down version of... you guessed it, python! Here are some python basics to get you started.

## Variables
Here is how you set variables. 

```python
age = 39
```

Here, `age` is the name of the variable and 39 is a number value that gets assigned to the variable. 

Here is another example, using text.
```python
name = "Adam"
``` 

## If Statements
One thing to know about python is white space (spaces and tabs) is important in python. There are no curly braces here. You use white space to show where a block of code begins and end.

Here is a super simple example, notice how the `print` command is indented.

```python
age = 39

if age >= 18:
  print("you can buy a lotto ticket now!")
```

Lets add another conditional:
```python
age = 22

if age >= 21:
  print("you can buy alcohol!")
else:
  print("it's ok, drinking is overrated.")
```

And here is one last conditional, with many options:
```python
age = 19

if age >= 21:
  print("full adult rights")
elif age >= 18:
  print("you can vote and gamble")
else:
  print("you'll grow up some day!)
```

## While Loops
While loop will run while a condition is true. This code will print "hello" six times.
```python
i = 0
while i < 6:
  print("hello")
  i += 1
```
 
Generally, we want to avoid continuous loops, but on a microcontroller, we often want our code to run forever, so you might see a 'forever loop' that looks like this.
```python
while True:
  print("running")
```
Anything inside the while loop will run forever. Ctrl-D in the mu editor will halt the code. 
 
## For loops
We can use a for loop to run a block of code a certain amount of times. This code does exactly the same output as the first while statement above.
```python
for x in range(6):
  print("hello")
```
Here, we are looping over a range of values from 0 to 6.

In python, it is easy to loop over an array of values.
```python
fruits = ["apple", "banana", "cranberry", "date"]
for fruit in fruits:
  print(fruit)
```

## Functions
We can write functions to make our code neat, organized, and repeatable. You define a function with the `def` keyword.
```python
def hello():
  print("hello")
```
And then we can call the function with `hello()`

A function can take in any number of values as parameters:
```python
def hello(name):
  print("hello " + name + "!")
```
Now we can greet specific people, `hello("adam")`
 
### Circuit Python "Hello World"
Let's look again at a simple CircuitPython "Hello World" flashy program, this time with comments.

```python
"""Example for Pico. Turns the built-in LED on and off with no delay."""
# import the time module form python core 
import time

# import different modules from circuitpython
import board
import digitalio

# assign the variable led to the boards led 
led = digitalio.DigitalInOut(board.LED) 
led.direction = digitalio.Direction.OUTPUT # set to output data.

while True: # forever loop
    led.value = True # turn the led on
    time.sleep(0.5) # delay half a second, keeps the led on
    led.value = False # turn the led off
    time.sleep(0.5) # delay, keeps the led off before repeat, otherwise it won't look like it ever turns off 
```

There is a lot more to learn here! Check out this resources to start your journey.

## Resource
- W3Schools [Python Guide](https://www.w3schools.com/python/default.asp)
- [CircuitPython](https://docs.circuitpython.org/en/latest/README.html) full documentation
- [Adafruite Guide](https://learn.adafruit.com/welcome-to-circuitpython/overview)
