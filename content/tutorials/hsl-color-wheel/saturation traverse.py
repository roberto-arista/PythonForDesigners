### Modules
from colorsys import hls_to_rgb

### Constants
FULL_CIRCLE = 360

### Variables
stripes = 20
isLuminosityConst = False
hueAngle = 120

### Instructions
newPage(400, 400)

stepWdt = width()/stripes

# iterate over the number of stripes
for ii in range(stripes):
    factor = ii / (stripes-1)

    # this conditional constructs allows the user
    # to switch the fixed parameter from luminosity to saturation
    if isLuminosityConst:
        rgbColor = hls_to_rgb(hueAngle/FULL_CIRCLE, .7, factor)
    else:
        rgbColor = hls_to_rgb(hueAngle/FULL_CIRCLE, factor, .7)

    # I love the unpacking operator 🤩
    fill(*rgbColor)
    rect(0, 0, stepWdt, height())
    translate(stepWdt, 0)
