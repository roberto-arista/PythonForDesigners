### Modules
from colorsys import hls_to_rgb

### Constants
FULL_CIRCLE = 360

### Instructions
newPage(400, 400)
# moving the reference point to the center of the canvas
# makes easier the rotation inside the for loop
translate(width()/2, height()/2)

# we iterate over 360° using a step of 10°
for angle in range(0, FULL_CIRCLE, 10):

    # both saturation and luminosity are fixed parameters
    rgbClr = hls_to_rgb(angle/FULL_CIRCLE, .7, .7)

    # graphic state context!
    # more info here
    # https://www.drawbot.com/content/canvas/state.html#managing-the-graphics-state
    with savedState():
        rotate(angle)
        translate(100, 0)
        fill(*rgbClr)
        oval(-4, -4, 8, 8)
