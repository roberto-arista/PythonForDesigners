### Modules
from colorsys import hls_to_rgb

### Constants
FULL_CIRCLE = 360

### Variables
cols = rows = 10
hueAngle = 240

### Instructions
newPage(400, 400)

stepWdt = width()/cols
stepHgt = height()/rows
for jj in range(rows):
    saturation = jj/(rows-1)
    for ii in range(cols):
        luminosity = ii/(cols-1)
        rgbClr = hls_to_rgb(hueAngle/FULL_CIRCLE, luminosity, saturation)
        fill(*rgbClr)
        rect(ii*stepWdt, jj*stepHgt, stepWdt, stepHgt)
