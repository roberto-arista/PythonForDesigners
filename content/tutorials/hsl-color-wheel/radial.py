### Modules
from colorsys import hls_to_rgb

### Constants
FULL_CIRCLE = 360
LINEAR_SCALE = 100

### Variables
hueStep = 5
linearStep = 10
isLuminosityConst = False
zz = .75

### Instructions
newPage(400, 400)
translate(width()/2, height()/2)

for angle in range(0, FULL_CIRCLE, hueStep):
    for linear in range(0, LINEAR_SCALE, linearStep):
        radius = 150 * linear/LINEAR_SCALE

        if isLuminosityConst:
            rgbClr = hls_to_rgb(angle/FULL_CIRCLE, zz, linear/LINEAR_SCALE)
        else:
            rgbClr = hls_to_rgb(angle/FULL_CIRCLE, linear/LINEAR_SCALE, zz)
        fill(*rgbClr)

        with savedState():
            rotate(angle)
            translate(radius, 0)
            oval(-4, -4, 8, 8)