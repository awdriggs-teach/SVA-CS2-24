# Absolute Basics 
This week we'll use [p5](https://p5js.org/) to explore how visualize can be made with code.
P5 is a javascript library that allows anyone to create interactive graphics.
It has simple functions to draw shapes to a canvas element and has pre-built "watchers" for user interactions (mouse and key clicks).

# Getting Started
P5 has a simple [web editor](https://editor.p5js.org/) that lets you get started in a flash.

Pressing the play button runs the code. Results can be scene in the preview window. Errors will be displayed in the console.

## Code Editor
The editor automatically loads some starter code, which every sketch needs to successfully run.

```javascript
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
}
```

I encourage you to change any of the numbers and see what happens.

`draw()` is a function (block of code) that p5 will run over an over again; it does its best to run at 60fps but sometimes the complexity of the code and browser might slow it down.

## Drawing a Circle
Try adding this line of code to the draw function: `ellipse(200, 200, 50, 50);` Click run and see what happens. Again, change any of the values to see what happens.

P5 has many other shape and drawing functions, check out the [reference](https://p5js.org/reference/) for a full list. 

## Using variables 
You can use variables to store data to be reused. For example you might want to change the size of multiple shapes together, so you create a size variable to hold onto that data. Check out this code.

```javascript
let size = 100; //declare and assign a variable.

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  ellipse(100, 100, size, size);
  ellipse(200, 200, size, size);
  ellipse(300, 300, size, size);
}
```
 
Now, if we want to change the size of all the circles, we can change the size variable to a different number and it will update all instances were we use `size`.

Change `let size = 100;` to `let size = 200;` and see what happens.
 
The best part of variables, is they can change, vary, over the course of the program. 

Try out this code:
```javascript
let size; //declare a variable for use later
function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  size = mouseX; //set size to value of the mouse's horizontal position.

  ellipse(100, 100, size, size);
  ellipse(200, 200, size, size);
  ellipse(300, 300, size, size);
}
```
Here we set `size` to the mouse's x, horizontal position in the canvas. `mouseX` is a built-in p5 variable that gets updated at the start of the draw loop.

## Doing Math
We can do all kinds of mathy stuff in p5. Change size to this: `size = width/2 - mouseX;`. Here, we are using another built-in variable, `width`, which is the size of the canvas, 400px. By dividing by 2 then subtracting the mouse x value, the circles get smaller as the mouse moves towards the center. Since there is no such thing as a negative size in p5, the circles get bigger as we move past the center towards the right.  

Often is is very helpful to see what is happening to the variables inside our program. We can use the `print` function to show the status of variables in the console.
Add these two lines to your draw function:
```javascript
print("x pos:", mouseX);
print("size:", size);
```
Now as the program runs the console spits out updates showing us the value of `mouseX` and the `size`.

Print statements are great for debugging but will effect the program as it runs, so you can delete them or add `//` to the front to comment them out. Any comments are ignored by the code interpreter. Comments are great way to leave notes for your future self!

## Next Steps
Learn more about drawing with p5 [here](https://awdriggs-teach.github.io/p5art/)
