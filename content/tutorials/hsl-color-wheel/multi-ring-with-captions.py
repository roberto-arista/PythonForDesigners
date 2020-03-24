### Modules
from colorsys import hls_to_rgb

### Constants
FULL_CIRCLE = 360
BLACK = 0, 0, 0

### Functions
def typeQualities(fontName='Arnold_v0.3-Regular', bodySize=9):
    # shout out to Rüdiger 👋
    font(fontName, bodySize)
    fill(*BLACK)
    stroke(None)

def lineQualities(clr=BLACK, thickness=1):
    stroke(*clr)
    strokeWidth(thickness)
    fill(None)


### Variables
isLuminosityConst = True
zz = .75
rings = 8

holeRadius = 45
ringThickness = 15

### Instructions
newPage(400, 400)
translate(width()/2, height()/2)

for angle in range(FULL_CIRCLE):
    for eachRing in range(rings):
        ringFactor = eachRing / (rings-1)
        radius = holeRadius + eachRing*ringThickness

        if isLuminosityConst:
            rgbClr = hls_to_rgb(angle/FULL_CIRCLE, zz, ringFactor)
        else:
            rgbClr = hls_to_rgb(angle/FULL_CIRCLE, ringFactor, zz)
        lineQualities(rgbClr, ringThickness)

        newPath()
        arc((0, 0), radius, angle-.5, angle+.5, clockwise=False)
        drawPath()

    with savedState():
        if angle % 10 == 0:
            captionRadius = radius + ringThickness
            rotate(angle)

            lineQualities(thickness=.5)
            line((captionRadius -2, 0), (captionRadius +2, 0))

            typeQualities()
            text(f'{angle}', (radius + ringThickness + 6, 0))
