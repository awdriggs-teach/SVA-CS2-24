# Working with Images
This guide will show you how to load and position images using p5.

## Loading an Image
We will want to load an image before the rest of the program load. p5 has a `preload` function that gets called before setup and draw. This is the place to load any media you are going to use in your sketch.
You will need to have the images loaded into the same folder as your `sketch.js` file.

```javascript
let img; //declare a variable for use later on.

function preload() {
  img = loadImage('./title.jpg'); //this image must be in the same folder as the sketch code
}
```

You can also use a url to access an image, but if that url ever changes you code break!
`img = loadImage('URL');`

## Display an Image
Inside `draw()`, add this line of code to display your image.

```javascript
function draw(){
  background(255); //white bg

  image(img, 200, 200);
}
```
The `image` function can take in a few parameters that determine which, and how the image is displayed.

  ```javascript
image(img, x, y, [width], [height])
  ```
  - `img`, the image object to display
  - `x`, the horizontal position, left side of the image
  - `y`, the vertical position, top side of the image
  - `width`, optional, sets the width
  - `height`, optional, sets the height

## Sizing
  Width and height can be set, they can stretch or squeeze an image. For example, change `draw()` to this:

  ```javasript
  function draw() {
    background(220);

    image(img, 0, 0, mouseX, mouseY);
  }
```
Now moving the mouse changes the size of image!

## Positioning an Image
The x and y position of the image refers to the top left corner of the image. A little math can be used to center an image.

```javascript
function draw() {
  background(220);
  let w = mouseX; //image width
  let h = mouseY; //image height
  image(img, width/2 - w/2, height/2 - h/2, w, h); //center image in the canvas
}
```

## "Paint" with the image
We can position the image however we like, for example we could have to follow the mouse.

```javascript
image(img, mouseX - img.width / 2, mouseY - img.height/2); //make it centered on the mouse
```

Now whenever we move the mouse the image follows. Try removing the `background()` at the start of draw. Now we can see a history of where the mouse has been.

We can easily make it so it only draws the image when the mouse is pressed. Wrap this around the image code.

```javascript
if(mouseIsPressed == true){ //only paint the image when the mosue is pressed.
  image(img, mouseX - img.width / 2, mouseY - img.height/2); 
}
```

# Next Steps
See how to manipulate pixel data in the [advanced images guide](./advanced.md)
