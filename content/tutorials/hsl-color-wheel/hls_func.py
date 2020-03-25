### Modules
from colorsys import hls_to_rgb

### Variables
hue = 120/360
saturation = 80/100
luminosity = 60/100

### Instructions
newPage(400, 400)
clr = hls_to_rgb(hue, luminosity, saturation)
print(clr)
fill(*clr)
rect(0, 0, width(), height())
