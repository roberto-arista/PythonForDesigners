### Modules
from colorsys import hls_to_rgb

### Constants
FULL_CIRCLE = 360

### Functions
def donut(slices):
    for eachSlice in range(slices):
        hueFactor = eachSlice/(slices-1)
        rgbClr = hls_to_rgb(hueFactor, .7, .7)
        stroke(*rgbClr)
        newPath()

        startAngle = (eachSlice-.5)/(slices-1) * FULL_CIRCLE
        endAngle = (eachSlice+.5)/(slices-1) * FULL_CIRCLE
        arc((0, 0), 100, startAngle, endAngle, clockwise=False)
        drawPath()

### Variables
slices = 15

### Instructions
newPage(952, 340)
translate(width()*.2, height()/2)

strokeWidth(30)
fill(None)
donut(4)

translate(width()*.3, 0)
donut(12)

translate(width()*.3, 0)
donut(36)


